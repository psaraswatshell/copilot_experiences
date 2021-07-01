func distinctsubstringcount(s string) int {
	if len(s) == 0 {
		return 0
	}
	if len(s) == 1 {
		return 1
	}
	set := make(map[string]struct{})

	for i := 0; i < len(s); i++ {
		for j := i + 1; j < len(s); j++ {
			set[s[i:j]] = struct{}{}
		}
	}
	return len(set)+1 //+1 for the whole string
}