from os import abort
import os
import extract_ppt
import text_to_image
import vedio_generation
import text_processing
from doodle_generator import doodle , doodle_2_vid
from flask import Flask, render_template, request
# from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
from flask import send_from_directory
app = Flask(__name__)

path = ""
PORT = int(os.environ.get("PORT", 3000))
img_folder = "frontend/src/assets/images"
vid_folder = "frontend/src/assets/video"
doodle_folder = "frontend/src/assets/doodle"
def get_file(path):
    # if request.method == 'POST':
    #     f = request.files['file']
    #     # path = ("ppt")
    #     f.save(path)
        
        ppt_ex = extract_ppt.data_extracter()
        pre_pro = text_processing.process_text()

        pro_df , pro_data = ppt_ex.extract(path)
        # data , pro_data = pre_pro.process(pro_data)

        img_gen = text_to_image.generate_images(img_folder)
        vid_gen  = vedio_generation.img_2_vid()

        res = False
        for sentence in pro_data:
            if(len(sentence.split())>2):
                res = img_gen.generate_deepAi(sentence)
                
        if(res =="Generated"):
            vid_gen.generate_video(img_folder,vid_folder)

            for f in os.listdir(img_folder):
                os.remove(os.path.join(img_folder,f))
        else:
            return "error"
        # try:
        return
            # return send_from_directory(vid_folder,"generated.avi")
        # except FileNotFoundError:
            # abort(404)

def generate_by_text(text):
    # text= request.get_data(as_text=True)
    pre_pro = text_processing.process_text()
    data , pro_data = pre_pro.process(text)

    img_gen = text_to_image.generate_images(img_folder)
    vid_gen  = vedio_generation.img_2_vid()
    doodle_gen = doodle_2_vid()
    res = False
    for sentence in pro_data:
        if(1):
            res = img_gen.generate_deepAi(sentence)
            doodle(sentence)
    if(res =="Generated"):
        doodle_gen.generate_video(doodle_folder,vid_folder)
        vid_gen.generate_video(img_folder,vid_folder)

        for f in os.listdir(img_folder):
            os.remove(os.path.join(img_folder,f))
        for f in os.listdir(doodle_folder):
            os.remove(os.path.join(doodle_folder,f))
        
    else:
        return "error"

    return
# get_file("/home/cnarte/better_education/presentationoncomputer-140406005455-phpapp02.pdf")
generate_by_text("bird is flying")