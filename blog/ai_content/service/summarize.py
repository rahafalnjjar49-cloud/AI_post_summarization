from venv import logger
from blog.models import Post
from .utils import validate_text_input, generate_ai_content, truncate_text


def _build_summarize_prompt(title: str) -> str:
    prompt = f"Please summarize the following blog post content:\n\n{title}"
    prompt += f"\nKeep the total output under 500 characters."
    return prompt


def summarize_post(post_id: int) -> dict:
    if not isinstance(post_id, int) or post_id <= 0:
        raise ValueError("Post ID must be a valid positive integer.")

    try:

        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise ValueError(f"Post with ID {post_id} does not exist.")

    cleaned_content = validate_text_input(post.content, min_length=1, field_name="Post content")
    prompt = _build_summarize_prompt(cleaned_content)

    try:
        raw_summary = generate_ai_content(prompt)
    except Exception as e:
        logger.error(f"Failed to summarize post {post_id}: {e}")
        raise


    cleaned_summary = truncate_text(raw_summary, max_length=500)

    return {
        "post_id": post.pk,
        "title": post.title,
        "summary": cleaned_summary,
        "length": len(cleaned_summary),
    }

