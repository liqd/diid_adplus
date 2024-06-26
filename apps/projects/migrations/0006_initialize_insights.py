# Generated by Django 3.2.19 on 2023-07-12 15:44

from apps import logger
from collections import defaultdict
from django.db import migrations


def initialize_insights(apps, schema_editor):
    ProjectInsight = apps.get_model("a4_candy_projects", "ProjectInsight")
    Comment = apps.get_model("a4comments", "Comment")
    Answer = apps.get_model("a4polls", "Answer")
    Vote = apps.get_model("a4polls", "Vote")
    Rating = apps.get_model("a4ratings", "Rating")
    Proposal = apps.get_model("a4_candy_budgeting", "Proposal")
    Idea = apps.get_model("a4_candy_ideas", "Idea")
    Like = apps.get_model("a4_candy_interactive_events", "Like")
    LiveQuestion = apps.get_model("a4_candy_interactive_events", "LiveQuestion")
    MapIdea = apps.get_model("a4_candy_mapideas", "MapIdea")

    insights = defaultdict(ProjectInsight)
    user_ids = defaultdict(set)

    for idea_model in [Idea, MapIdea, Proposal]:
        for idea_object in idea_model.objects.all().select_related(
            "creator", "module__project"
        ):
            project = idea_object.module.project
            insights[project].written_ideas += 1
            user_ids[project].add(idea_object.creator.id)

    for live_question in LiveQuestion.objects.all().select_related("module__project"):
        insights[live_question.module.project].live_questions += 1

    for answer in Answer.objects.all().select_related(
        "creator",
        "question__poll__module__project",
    ):
        project = answer.question.poll.module.project
        insights[project].poll_answers += 1
        user_ids[project].add(answer.creator.id)

    for vote in Vote.objects.all().select_related(
        "creator",
        "choice__question__poll__module__project",
    ):
        project = vote.choice.question.poll.module.project
        insights[project].poll_answers += 1
        user_ids[project].add(vote.creator.id)

    for comment in Comment.objects.exclude(project=None).select_related(
        "project", "creator"
    ):
        project = comment.project
        insights[project].comments += 1
        user_ids[project].add(comment.creator.id)

    for like in Like.objects.all().select_related("livequestion__module__project"):
        project = like.livequestion.module.project
        insights[project].ratings += 1

    for rating in Rating.objects.all().select_related("creator", "content_type"):
        model_name = rating.content_type.model
        content_model = apps.get_model(
            app_label=rating.content_type.app_label,
            model_name=model_name,
        )
        content_object = content_model.objects.get(id=rating.object_pk)

        if model_name == "comment":
            project = content_object.project
        elif model_name in ["idea", "mapidea", "topic", "proposal"]:
            project = content_object.module.project
        else:
            logger.warning(f"could not identify project: {rating=}")
            continue

        insights[project].ratings += 1
        user_ids[project].add(rating.creator.id)

    for project, insight in insights.items():
        insight.project = project
        insight.save()

        if user_ids[project]:
            insight.active_participants.add(*user_ids[project])


def delete_insights(apps, schema_editor):
    ProjectInsight = apps.get_model("a4_candy_projects", "ProjectInsight")
    ProjectInsight.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("a4_candy_projects", "0005_projectinsight"),
        ("a4polls", "0005_verbose_name_created_modified"),
        ("a4ratings", "0004_verbose_name_created_modified"),
        ("a4_candy_topicprio", "0002_topic_description_add_verbose_name"),
        ("a4comments", "0013_set_project"),
    ]

    operations = [
        migrations.RunPython(code=initialize_insights, reverse_code=delete_insights),
    ]
