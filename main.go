package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"math/rand"
	"os"
	"time"
)

const (
	lowerChars   = "abcdefghijklmnopqrstuvwxyz"
	upperChars   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	numberChars  = "0123456789"
	symbolChars  = "!@#$%^&*()_-+=<>?,."
	allCharSet   = lowerChars + upperChars + numberChars + symbolChars
	defaultLength = 12
)

type Password struct {
	Value string `json:"password"`
}

func generatePassword(length int) string {
	rand.Seed(time.Now().UnixNano())

	password := make([]byte, length)
	charSetLength := len(allCharSet)

	for i := 0; i < length; i++ {
		randomIndex := rand.Intn(charSetLength)
		password[i] = allCharSet[randomIndex]
	}

	return string(password)
}

func savePasswordToFile(password string) error {
	pwd := Password{Value: password}
	data, err := json.MarshalIndent(pwd, "", "  ")
	if err != nil {
		return err
	}

	err = ioutil.WriteFile("password.json", data, 0644)
	if err != nil {
		return err
	}

	return nil
}

func main() {
	password := generatePassword(defaultLength)
	fmt.Println("Generated Password:", password)

	var saveOption string
	fmt.Print("Do you want to save the password to a file? (y/n): ")
	fmt.Scanln(&saveOption)

	if saveOption == "y" {
		err := savePasswordToFile(password)
		if err != nil {
			fmt.Println("Error saving password:", err)
		} else {
			fmt.Println("Password saved to password.json")
		}
	}
}

