# Commands dan Fitur yang ada pada git

## Perintah-perintah dasar

Inisialisasi git

```bash
git init
```

Menambahkan files pada git

```bash
git add .
git add README.md
```

Melihat status git

```bash
git status
```

Melakukan commit

```bash
git commit -m "pesan"
```

Git branch

```bash
git branch #melihat branch local
git branch -d {localBranchName} #menghapus local branch
git branch -r #melihat branch local buat remote
```

Melakukan push

```bash
git push origin HEAD:{remoteBranch} #push ke beda branch dari current branch local
git push -u origin master #push ke master branch
git push -f origin master #push ke master dengan force
git push origin --delete {remoteBranchName} #untuk menghapus branch remote secara local
```

Melakukan pull

```bash
git pull origin master #pull biasa dari branch master
git pull origin master --allow-unrelated-histories #pull dengan allowing histories yang beda dari master
```

Git remote

```bash
git remote remove origin #menghapus repo remote dengan nama origin
git remote add origin https://github.com/YourUsername/YourRepo.git #menambahkan remote repo dgn nama origin
git config --get remote.origin.url #get remote url
git remote show origin #show origin url
```

Git checkout

```bash
git checkout -b ＜new-branch＞ #membuat dan pindah ke branch baru secara local
git checkout {name branch} #pindah ke sebuah branch secara lokal
```

Git clone

```bash
git clone https://github.com/reyhannaufal/soal-shift-sisop-modul-1-A04-2021.git #Cloning repo git
```

## Fitur pada readme git

Hyperlink

```bash
[{teks-yang-ditampilkan}]({link})
```

Image/gif

```bash
![alt text]({link-gambar}) <br />
```
