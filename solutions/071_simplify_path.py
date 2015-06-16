# Given an absolute path for a file (Unix-style), simplify it.

# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"

# click to show corner cases.
# Corner Cases:

#     Did you consider the case where path = "/../"?
#     In this case, you should return "/".
#     Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
#     In this case, you should ignore redundant slashes and return "/home/foo".


class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        
        currentPath = []
        dirs = filter(None, path.split("/"))
        for d in dirs:
            if d == '.':
                continue

            if d == "..":
                if currentPath:
                    currentPath.pop()
                continue
            
            currentPath.append(d)

        return "/" + "/".join(currentPath)



