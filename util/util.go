package util

import (
	"strings"
	"unicode"
)

// remove all non-alphabet characters
func GetStripWord(word string) string {
	word = strings.ToLower(word)
	// remove all non-alnum characters
	if !isalnumStr(word) {
		var newWord strings.Builder
		for _, c := range word {
			if isalnumRune(c) {
				newWord.WriteRune(c)
			}
		}
		return newWord.String()
	}
	return word
}

// python equivalent `string.isalnum()`
func isalnumStr(word string) bool {
	for _, c := range word {
		if !isalnumRune(c) {
			return false
		}
	}
	return true
}

// python equivalent `string.isalnum()`
func isalnumRune(c rune) bool {
	return unicode.IsLetter(c) || unicode.IsNumber(c)
}
