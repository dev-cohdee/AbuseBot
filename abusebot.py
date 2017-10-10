import praw
import os

reddit = praw.Reddit('bot1')

if not os.path.isfile("posts_replied_to.txt"):
	posts_replied_to = []
	
else:
	with open("posts_replied_to.txt", "r") as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit('joinsquad')

for submission in subreddit.new(limit=5):
	print('Submission Title: ', submission.title)
	questions = ['admin abuse ', 'abuse admin power', 'admin banned', 'banned from server', 'perma-banned', 'permanantly banned', 'kicked from server', 'admin kicked', 'banned from']
	normalized_title = submission.title.lower()
	for question_phrase in questions:
		if question_phrase in normalized_title:
			if submission.id not in posts_replied_to:

				reply_template = '**Witnessed or experienced admin abuse?** **Visit** http://forums.joinsquad.com/forum/241-report-server-admin-abuse/ ^developed ^by: ^cohdee90'
		
				url_title = submission.title
				reply_text = reply_template.format(url_title)
				print('Replying to:',url_title)
				submission.reply(reply_text)
				posts_replied_to.append(submission.id)
				with open("posts_replied_to.txt", "w") as f:
					for posts_id in posts_replied_to:
						f.write(posts_id + "\n")
				