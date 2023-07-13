class DNA2:
    def get_reverse_sequence(self, seq: str) -> str:
        """입력 받은 seq의 reverse 서열을 반환합니다

        Args:
            seq (str): 서열 문자열

        Returns:
            str: reversed sequence

        Examples:
        >>> dna.get_reverse_sequence("AATTGGCC")
        """
        return seq[::-1]


if __name__ == "__main__":
    dna = DNA2()
    rev_seq = dna.get_reverse_sequence("AATTGGCC")
    print(rev_seq)
