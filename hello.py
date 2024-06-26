print("Hello from Binder!")

echo "# my-first-binder" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Z5app/my-first-binder.git
git push -u origin main
