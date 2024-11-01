package coca60000

import (
	_ "embed"
	"strconv"
	"strings"

	"github.com/fondoger/go-wordnet-db/util"
)

//go:embed coca60000-rank.txt
var rawData string

var Coca60000Stripped map[string]int

func init() {
	Coca60000Stripped = make(map[string]int)

	lines := strings.Split(rawData, "\n")
	for _, line := range lines {
		if line == "" {
			continue
		}
		parts := strings.Split(line, "|")
		word := util.GetStripWord(parts[0])
		rank, _ := strconv.Atoi(parts[1])
		Coca60000Stripped[word] = rank
	}
}
