#coding:utf-8

class Convert(object):



    @classmethod
    def convert(self,papers):
        str = ''
        with open('D:\markdown.txt','w') as file_writer:
            for p in papers:
                if p['tag']=='text':
                    str = p['content'].replace('c_start','**').replace('c_end','**')
                    pass
                elif p['tag']=='code':
                    str = '```'+'\r\n'+p['content']+'\r\n'+'```'

                else:
                    #![](http://upload-images.jianshu.io/upload_images/1823443-7c4c920514b8f0cf.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
                    str = '![](%s)'%(p['content'])
                    str = '\r\n'+str+'\r\n'

                file_writer.write(str.encode('utf-8'))
                file_writer.write('\r\n'.encode('utf-8'))

        file_writer.close()

