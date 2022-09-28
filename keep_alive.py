from threading import Thread

Khela_Hobe_Mehrabbai = Flask('')

@Khela_Hobe_Mehrabbai.route('/')
def home() :
  return "UUUHH, Beche Achi Alhamdulillah!"

def run() :
  Khela_Hobe_Mehrabbai.run(host = '0.0.0.0', port = 8080)

def keep_alive() :
  Cholo_Bohudur = Thread(target = run)
  Cholo_Bohudur.start()
