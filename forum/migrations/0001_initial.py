# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import forum.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('accounts', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name=b'Forum title')),
                ('description', models.CharField(max_length=250, verbose_name=b'Forum description')),
                ('priority', models.PositiveSmallIntegerField(default=0, help_text=b'Smaller the value, higher the position', verbose_name=b'Forum list priority')),
                ('topics_count', models.PositiveIntegerField(default=0, verbose_name=b'Number of topics')),
                ('posts_count', models.PositiveIntegerField(default=0, verbose_name=b'Number of posts')),
            ],
            options={
                'ordering': ['priority'],
                'verbose_name': 'Forum',
                'verbose_name_plural': 'Forums',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('can_change_group_topic', models.BooleanField(default=False, verbose_name='Can change any topics')),
                ('can_move_group_topic', models.BooleanField(default=False, verbose_name='Can move any topics')),
                ('can_split_group_topic', models.BooleanField(default=False, verbose_name='Can split any topics')),
                ('can_delete_group_topic', models.BooleanField(default=False, verbose_name='Can delete any topics')),
                ('can_stick_group_topic', models.BooleanField(default=False, verbose_name='Can stick any topics')),
                ('can_close_group_topic', models.BooleanField(default=False, verbose_name='Can close any topics')),
                ('can_change_group_post', models.BooleanField(default=False, verbose_name='Can change any posts')),
                ('can_move_group_post', models.BooleanField(default=False, verbose_name='Can move any posts')),
                ('can_delete_group_post', models.BooleanField(default=False, verbose_name='Can delete any posts')),
                ('can_add_own_topic', models.BooleanField(default=False, verbose_name='Can add topics')),
                ('can_change_own_topic', models.BooleanField(default=False, verbose_name='Can change own topics')),
                ('can_delete_own_topic', models.BooleanField(default=False, verbose_name='Can delete own topics')),
                ('can_close_own_topic', models.BooleanField(default=False, verbose_name='Can close own topics')),
                ('can_add_own_post', models.BooleanField(default=False, verbose_name='Can add posts')),
                ('can_change_own_post', models.BooleanField(default=False, verbose_name='Can chage own posts')),
                ('can_delete_own_post', models.BooleanField(default=False, verbose_name='Can delete own posts')),
                ('forum', models.ForeignKey(verbose_name='Forum', to='forum.Forum')),
                ('group', models.ForeignKey(verbose_name='Forum group', to='accounts.Group')),
            ],
            options={
                'ordering': ['forum'],
                'verbose_name': 'Permission',
                'verbose_name_plural': 'Permissions',
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name=b'title')),
                ('total_votes', models.PositiveIntegerField(default=0, verbose_name=b'Total number of votes')),
                ('expires', models.DateField(null=True, verbose_name=b'Poll expiration date', blank=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Poll',
                'verbose_name_plural': 'Polls',
            },
        ),
        migrations.CreateModel(
            name='PollChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name=b'Choice')),
                ('votes_count', models.PositiveIntegerField(default=0, verbose_name=b'Number of votes')),
                ('poll', models.ForeignKey(related_name='choices', verbose_name=b'Poll', to='forum.Poll')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Poll choice',
                'verbose_name_plural': 'Poll choices',
            },
        ),
        migrations.CreateModel(
            name='PollVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'Vote date')),
                ('choice', models.ForeignKey(related_name='votes', verbose_name=b'Poll choice', to='forum.PollChoice')),
                ('poll', models.ForeignKey(related_name='votes', verbose_name=b'Poll', to='forum.Poll')),
                ('profile', models.ForeignKey(verbose_name=b'User', to='accounts.UserProfile')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Poll vote',
                'verbose_name_plural': 'Poll votes',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'Post date')),
                ('ip_address', models.GenericIPAddressField(null=True, verbose_name=b'IP Address', blank=True)),
                ('message', models.TextField(max_length=32000, verbose_name=b'Original bbCode message')),
                ('message_html', models.TextField(verbose_name=b'Compiled HTML message')),
                ('is_removed', models.BooleanField(default=False, verbose_name=b'Is removed')),
                ('profile', models.ForeignKey(verbose_name=b'User', to='accounts.UserProfile')),
            ],
            options={
                'ordering': ['date'],
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='ReadTracking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_read', forum.fields.SerializedField(blank=True)),
                ('profile', models.OneToOneField(to='accounts.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('profile', models.ForeignKey(related_name='forum_subscription', to='accounts.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name=b'Topic title')),
                ('posts_count', models.PositiveIntegerField(default=0, verbose_name=b'Number of posts')),
                ('is_sticky', models.BooleanField(default=False, verbose_name=b'Is sticky')),
                ('is_closed', models.BooleanField(default=False, verbose_name=b'Is closed')),
                ('is_removed', models.BooleanField(default=False, verbose_name=b'Is removed')),
                ('first_post', models.ForeignKey(related_name='first_for_topic', verbose_name=b'First post', blank=True, to='forum.Post', null=True)),
                ('forum', models.ForeignKey(verbose_name=b'Forum', to='forum.Forum')),
                ('last_post', models.ForeignKey(related_name='last_for_topic', verbose_name=b'Last post', blank=True, to='forum.Post', null=True)),
            ],
            options={
                'ordering': ['-is_sticky', '-last_post__date'],
                'verbose_name': 'Topic',
                'verbose_name_plural': 'Topics',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(verbose_name=b'Topic', to='forum.Topic'),
        ),
        migrations.AddField(
            model_name='poll',
            name='topic',
            field=models.ForeignKey(related_name='polls', verbose_name=b'Topic', to='forum.Topic'),
        ),
        migrations.AddField(
            model_name='forum',
            name='last_post',
            field=models.ForeignKey(verbose_name=b'Last post', blank=True, to='forum.Post', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='permission',
            unique_together=set([('group', 'forum')]),
        ),
    ]
