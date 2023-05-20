# Gen 

## This program is a password manager command line program that you can use as your password manager in the cli 


## Prequistites 

- you will need git if you dont have it installed then install it with your package manager on linux 

- Debian 

```
sudo apt install git 
```

- Fedora 

```
sudo dnf install git 
```
- Arch

```
sudo pacman -S git 
```

- Then grab the program by doing 

```
git clone https://github.com/freidhofkyle/gen.git
```




## How to use these programs

- The options 

```
-d = This will decrypt the file  
```

```
-e = This will encrypt the file 
```

```
-f = will give you the option to save it to what ever filename you choose 
```

```
-l = will give you the option to specify the size of the password you want 
```

```
-u = will allow you to specify the username for what ever password you are creating 
```

- examples of how to use it 

```
python3 -u user -l 12 -f foo.txt -e
```

```
python3 -f foo.txt -d 

```
- Also it will give you and encryption key do not lose it or give it to anyone else that is not you and remember your encryption key 




