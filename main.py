import post as pc

with open('text.txt', mode='r', encoding='utf-8') as text_file:
    texts = text_file.readlines()
for x, text in enumerate(texts):
    img = pc.create_content(path= 'images/'+str(x+1)+'.jpg', text=text, text_color=(255, 255, 255), back_color=(255, 0, 0, 50), font='arial.ttf', pos='post')
    img.save('images/'+str(x+1)+'_new_post.jpg')