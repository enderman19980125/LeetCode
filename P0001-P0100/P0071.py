class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace("//", "/").strip("/")
        directories = path.split("/")
        simplified_directories = []
        for directory in directories:
            if directory in [".", ""]:
                continue
            elif directory == "..":
                if simplified_directories:
                    simplified_directories.pop()
            else:
                simplified_directories.append(directory)
        simplified_path = "/" + "/".join(simplified_directories)
        return simplified_path


if __name__ == '__main__':
    solution = Solution()

    answer = solution.simplifyPath("/home/")
    print(answer, "/home")

    answer = solution.simplifyPath("/../")
    print(answer, "/")

    answer = solution.simplifyPath("/home//foo/")
    print(answer, "/home/foo")

    answer = solution.simplifyPath("/a/./b/../../c/")
    print(answer, "/c")

    answer = solution.simplifyPath("/a/../../b/../c//.//")
    print(answer, "/c")

    answer = solution.simplifyPath("/a//b////c/d//././/..")
    print(answer, "/a/b/c")
