#!/usr/bin/python3

import asyncio
import tornado
import os
import random
import string

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        file1 = self.request.files['file1'][0]
        original_fname = file1['filename']
        extension = os.path.splitext(original_fname)[1]
        print(extension)
        if extension == ".mp4" or extension == ".png" or extension == ".jpg" or extension == ".jpeg":
            fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
            final_filename= fname+extension
            output_file = open("website/uploads/" + final_filename, 'wb')
            output_file.write(file1['body'])
            self.finish("file" + final_filename + " is uploaded")
        else:
            self.finish("Не подходит")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/upload", UploadHandler)
    ], autoreload=True, debug=True)

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
