docker build -t vision-ai-image .
docker run --name vision-ai-container -d -p 8000:8000 -v $(pwd):/code vision-ai-image

#connect to turborepo
git subtree add --prefix=apps/vision-ai https://github.com/valiantlynx/vision-ai.git main --squash
git subtree pull --prefix=apps/vision-ai https://github.com/valiantlynx/vision-ai.git main --squash
git subtree push --prefix=apps/vision-ai https://github.com/valiantlynx/vision-ai.git main