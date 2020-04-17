"""
Return 1 if version 1 > version 2
Return -1 if version 2 > version 1
Return 0 if version 1 == version 2

Ignore leading zeros

Idea, split by '.' for the versionsx


"""

######
# Two pointer approach, implies no need for extra space O(N + M)
#
#
#####


def compare_version(version1: str, version2: str) -> int:
    
        versions1_revisions = list(map(lambda x: int(x), version1.split('.')))
        versions2_revisions = list(map(lambda x: int(x), version2.split('.')))

        # version1 < version2 return -1
        # versions1 > version2 return 1
        # version1 = version2 return 0

        # If they're the same keep iterating

        v1_length = len(versions1_revisions)
        v2_length = len(versions2_revisions)

        if v1_length < v2_length:
            versions1_revisions = versions1_revisions + [0] * (v2_length - v1_length)
        elif v2_length < v1_length:
            versions2_revisions = versions2_revisions + [0] * (v1_length - v2_length)

        for i in range(max(v1_length, v2_length)):

            if versions1_revisions[i] < versions2_revisions[i]:
                return -1
            if versions1_revisions[i] > versions2_revisions[i]:
                return 1

        return 0







if __name__ == "__main__":
    
    output = compare_version('0.1', '1.1')
