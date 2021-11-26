cd ..
sudo docker build -t myimage -f api/Dockerfile .
sudo docker run -d --name mycontainer  myimage

