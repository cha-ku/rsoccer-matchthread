

import praw
#import pprint

sub_id = raw_input("Enter the submission id of the text post: ")

r = praw.Reddit(user_agent = 'cmdlinesoccer')

mtch_thread = r.get_submission(submission_id = sub_id)

getKickOff_index = mtch_thread.selftext.lower().find("1'")

print(mtch_thread.selftext[getKickOff_index : ])
