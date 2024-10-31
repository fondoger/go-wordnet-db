package coca60000

import (
	_ "embed"
	"strconv"
	"strings"
)

//go:embed coca60000-rank.txt
var rawData string

var Coca60000 map[string]int

func init() {
	Coca60000 = make(map[string]int)

	lines := strings.Split(rawData, "\n")
	for _, line := range lines {
		if line == "" {
			continue
		}
		parts := strings.Split(line, "|")
		word := parts[0]
		rank, _ := strconv.Atoi(parts[1])
		Coca60000[word] = rank
	}
}
