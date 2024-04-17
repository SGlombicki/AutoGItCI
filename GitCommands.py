import os

def deleteProject():

	os.system("rm -rf /discord-bot")

	return 0;

def downloadProject():
	gittoken = os.environ.get('GITHUB_PAT')
	os.system("git clone https://sglombicki:" + gittoken + "@github.com/sglombicki/GUSCCDBot.git /discord-bot")

	return 0;

def serviceChange(state):
	if state == "Stop":
		os.system('systemctl stop ddbot')
		return 0;
	elif state == "Start":
		os.system("systemctl start ddbot")
		return 0;

def gitChange():
	serviceChange("Stop")
	deleteProject()
	downloadProject()
	serviceChange("Start")
	return 0;