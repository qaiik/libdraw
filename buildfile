chmod +x draw.py
mkdir ~/LibDRAW 
cp ./draw.py ~/LibDRAW/maindraw.py
echo "python3 maindraw.py $*" > ~/LibDRAW/cmd.sh
chmod +x ~/LibDRAW/cmd.sh
echo "alias draw=\"~/LibDRAW/cmd.sh \"" >> ~/.zshrc
