import tornado.ioloop
import tornado.web
import os, sys
import json
from datetime import datetime

LINE = None
BAR = None
PIE = None
with open('view/FB-DISCUSSION-FREQ_%s_%s.json'%(sys.argv[1], sys.argv[2])) as f:
    LINE = json.load(f)
with open('view/FB-WORD-TFIDF_%s_%s.json'%(sys.argv[1], sys.argv[2])) as f:
    BAR = json.load(f)
with open('view/FB-MOOD-SUM_%s_%s.json'%(sys.argv[1], sys.argv[2])) as f:
    PIE = json.load(f)
last_update_time = datetime.today().strftime('%B %d, %Y')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        
        pie_colors = ['#28a745', '#dc3545', '#007bff', '#ffc107']
        
        self.render("index.html", last_update_time=last_update_time,
                                    line_labels=[ D['date'] for D in LINE ],
                                    line_datas=[ D['count'] for D in LINE ],
                                    bar_labels=[ D['word'] for D in BAR ],
                                    bar_datas=[ D['tfidf'] for D in BAR ],
                                    pie_labels=list(PIE.keys()),
                                    pie_datas=[ PIE[k] for k in PIE.keys() ],
                                    pie_colors=pie_colors[:len(list(PIE.keys()))])
                                    
class UpdateDataHandler(tornado.web.RequestHandler):
    def get(self):
        since = self.get_argument('starttime', sys.argv[1])
        until = self.get_argument('endtime', sys.argv[2])
        with open('view/FB-DISCUSSION-FREQ_%s_%s.json'%(since, until)) as f:
            LINE = json.load(f)
        with open('view/FB-WORD-TFIDF_%s_%s.json'%(since, until)) as f:
            BAR = json.load(f)
        with open('view/FB-MOOD-SUM_%s_%s.json'%(since, until)) as f:
            PIE = json.load(f)
        last_update_time = datetime.today().strftime('%B %d, %Y')

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "autoreload": True
}

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/update", UpdateDataHandler)
    ], **settings)

if __name__ == "__main__":
    PORT = int(sys.argv[3])
    print('listen on port: %d'%PORT)
    app = make_app()
    app.listen(the_port)
    tornado.ioloop.IOLoop.current().start()
    
    
    
    
    