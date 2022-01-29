import wget  
# downloads = []
# while True:
#   file_url = input("Masukkan Link : ")
#   if(file_url.lower() == 'exit'):
#     break
#   downloads.append(file_url)

file_url = input("Masukkan Link : ")
downloads = file_url.split(',')


# print(file_url)
# output = "/content/drive/My Drive/Download/"
print('start downloading')
# wget.download(file_url,out=output)
# !wget "https://cloud1.send.cm/d/djyudccc6gosj4l4an2udd55y3uccivoipi7hvsce57ucfhn2v3demxlr4h736cm25zirwg6/codecourse-podcast.part2.rar" -P "/content/drive/My Drive/Download/"
# !wget -A rar {file_url} -P "/tmp"
for i in downloads:
  !wget {i} -P "/tmp"
  print('Finish download\n')