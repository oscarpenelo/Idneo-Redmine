display_usage() { 
    echo "REDMINE IDNEO - BY OSCAR PENELO" 
    echo -e "\n./start.sh -u [username] -p [password] -i [issue] \n" 
    } 


if [ $# -eq 0 ]
  then
    display_usage
    exit 0
fi
while getopts u:p:i: option
do
case "${option}"
in
u) USER=${OPTARG};;
p) PASS=${OPTARG};;
i) ISSUE=${OPTARG};;
esac
done
sudo docker rm -f idneoredmine

sudo docker build -t idneoredmine .




echo ISSUE $ISSUE
sudo docker run --restart=always -d --name idneoredmine -p 80 -i -t idneoredmine python redmine.py -u $USER -p $PASS -i $ISSUE -d
