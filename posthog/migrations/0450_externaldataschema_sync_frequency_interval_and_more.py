# Generated by Django 4.2.14 on 2024-07-24 10:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0449_alter_plugin_organization_alter_plugin_plugin_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="externaldataschema",
            name="sync_frequency_interval",
            field=models.DurationField(blank=True, null=True, default=datetime.timedelta(seconds=21600)),
        ),
        migrations.RunSQL(
            sql="""
                UPDATE posthog_externaldataschema
                SET sync_frequency_interval = interval '24 hour'
                WHERE sync_frequency = 'day';
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.RunSQL(
            sql="""
                UPDATE posthog_externaldataschema
                SET sync_frequency_interval = interval '7 day'
                WHERE sync_frequency = 'week';
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.RunSQL(
            sql="""
                UPDATE posthog_externaldataschema
                SET sync_frequency_interval = interval '30 day'
                WHERE sync_frequency = 'month';
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.AlterField(
            model_name="externaldataschema",
            name="sync_frequency",
            field=models.CharField(
                blank=True,
                choices=[("day", "Daily"), ("week", "Weekly"), ("month", "Monthly")],
                default="day",
                max_length=128,
                null=True,
            ),
        ),
    ]