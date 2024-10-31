package etymology

import (
	"bufio"
	"bytes"
	_ "embed"
	"log"
	"strings"
)

// Comma separated string lines
//
//go:embed etymology-en.csv
var rawData []byte

var Etymology map[string]string

const (
	RelTypeHasSuffix         = 0
	RelTypeHasSuffixWithRoot = 1
	RelTypeHasPrefix         = 2
	RelTypeHasPrefixWithRoot = 3
	RelTypeHasAffix          = 4
	RelTypeHasConfix         = 5
	RelTypeDoubletWith       = 6
	RelTypeCompoundOf        = 7
	RelTypeBlendOf           = 8
	RelTypeClippingOf        = 9
	RelTypeCognateOf         = 10
	RelTypeAbbreviationOf    = 11
	RelTypeIsOnomatopoeic    = 12
	RelTypeBackFormationFrom = 13
	RelTypeDerivedFrom       = 14
)

var relTypeMapping = map[string]string{
	"has_suffix":           "00",
	"has_suffix_with_root": "01",
	"has_prefix":           "02",
	"has_prefix_with_root": "03",
	"has_affix":            "04",
	"has_confix":           "05",
	"doublet_with":         "06",
	"compound_of":          "07",
	"blend_of":             "08",
	"clipping_of":          "09",
	"cognate_of":           "10",
	"abbreviation_of":      "11",
	"is_onomatopoeic":      "12",
	"back-formation_from":  "13",
	"derived_from":         "14",
}

func init() {
	Etymology = make(map[string]string)

	reader := bufio.NewReader(bytes.NewReader(rawData))

	line, _, err := reader.ReadLine()
	for err == nil {
		if len(line) == 0 {
			line, _, err = reader.ReadLine()
			continue
		}
		parts := strings.Split(string(line), ",")
		if len(parts) != 3 {
			log.Fatalf("Invalid line: %s", line)
		}
		word := parts[0]
		reltype := parts[1]
		target := parts[2]
		typ, ok := relTypeMapping[reltype]
		if !ok {
			log.Fatalf("Invalid relation type: %s", reltype)

		}
		Etymology[word] = typ + target

		line, _, err = reader.ReadLine()
	}
}
