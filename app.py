import gradio as gr
from dotenv import load_dotenv
from Ingest.answer import answer_question

load_dotenv(override=True)


def format_context(context):
    if not context:
        return "*No context retrieved.*"

    result = ""
    for doc in context:
        source   = doc.metadata.get("source", "Unknown")
        section  = doc.metadata.get("source_section", "")
        doc_type = doc.metadata.get("doc_type", "")

        result += f"**Source:** `{source}`"
        if doc_type:
            result += f" · **Type:** `{doc_type}`"
        if section:
            result += f"\n\n**Section:** {section}"
        # page_content guard — should never be None but defensive check
        result += f"\n\n{doc.page_content or '*No content available.*'}\n\n---\n\n"

    return result.strip()


def put_message_in_chatbot(message, history):
    # guard — ignore empty or whitespace-only submissions
    if not message or not message.strip():
        return message, history
    return "", history + [{"role": "user", "content": message.strip()}]


def chat(history):
    # guard — should never be empty but defensive check
    if not history:
        return history, "*No question received.*"

    last_message = history[-1]["content"]
    prior        = history[:-1]

    try:
        answer, context = answer_question(last_message, prior)
        history.append({"role": "assistant", "content": answer})
        return history, format_context(context)

    except Exception as e:
        # keep the conversation alive — show error as assistant message
        print(f"[chat] Error: {type(e).__name__}: {e}")
        error_msg = (
            "⚠️ Something went wrong while answering your question. "
            "Please try again.\n\n"
            f"*Error: {type(e).__name__}*"
        )
        history.append({"role": "assistant", "content": error_msg})
        return history, "*Error retrieving context.*"


def main():

    theme = gr.themes.Soft(font=["Inter", "system-ui", "sans-serif"])

    with gr.Blocks(title="Adaptive RAG Assistant", theme=theme) as ui:

        gr.Markdown("# 🏢 Adaptive RAG Assistant\nAsk me anything about your documents!")

        # ── Chat area ──────────────────────────────────────────────────────
        chatbot = gr.Chatbot(
            label="💬 Conversation",
            height=500,
            type="messages",
            show_copy_button=True,
        )

        # ── Message input + send button ────────────────────────────────────
        with gr.Row():
            message = gr.Textbox(
                placeholder="Write a message...",
                show_label=False,
                scale=9,
                container=False,
            )
            send_btn = gr.Button(
                value="➤",
                scale=1,
                variant="primary",
                min_width=20,
            )

        # ── Collapsible context panel at bottom ────────────────────────────
        with gr.Accordion("📚 Retrieved Context — click to expand", open=False):
            context_display = gr.Markdown(
                value="*Ask a question to see retrieved context here.*"
            )

        # ── Event chain — Enter key and send button trigger same flow ──────
        submit_inputs  = [message, chatbot]
        submit_outputs = [message, chatbot]
        chat_inputs    = [chatbot]
        chat_outputs   = [chatbot, context_display]

        message.submit(
            put_message_in_chatbot, submit_inputs, submit_outputs
        ).then(
            chat, chat_inputs, chat_outputs
        )

        send_btn.click(
            put_message_in_chatbot, submit_inputs, submit_outputs
        ).then(
            chat, chat_inputs, chat_outputs
        )

    ui.launch(inbrowser=True)


if __name__ == "__main__":
    main()