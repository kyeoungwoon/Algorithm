import os

urls = [
    'https://youtube.com/playlist?list=PLONB62YjBmH3gbK5ENl8QErUBdGzuN9ws',
    'https://youtube.com/playlist?list=PLucdnvOsr3ss4vimHlpSY9PHVXOQIFSmM',
    'https://www.youtube.com/watch?v=zo8ZxIp88SM&list=PLucdnvOsr3svZb1QwIz039cu9ySOUVhn1&index=2',
    'https://www.youtube.com/watch?v=39bVN8A4Ia0&list=PLucdnvOsr3svZb1QwIz039cu9ySOUVhn1&index=3',
    'https://www.youtube.com/watch?v=YcTwsmqsnZ8&list=PLucdnvOsr3svZb1QwIz039cu9ySOUVhn1&index=4',
    'https://www.youtube.com/watch?v=5kGF8wyNt2Q&list=PLucdnvOsr3sud8PsjyhLQVyrkrUpjJz69&index=1',
    'https://www.youtube.com/watch?v=fsys7_MutCo&list=PLucdnvOsr3sud8PsjyhLQVyrkrUpjJz69&index=2'
    
]

for url in urls:
    os.system(f"youtube-dl {url} -x --audio-format best --audio-quality 0 -i")