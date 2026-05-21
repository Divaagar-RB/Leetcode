class Solution:
    def distanceK(self, root, target, k):

        ans = []

        def collect_k_down(node, d):

            if not node:
                return

            if d == 0:
                ans.append(node.val)
                return

            collect_k_down(node.left, d - 1)
            collect_k_down(node.right, d - 1)

        def find_target_dist(node):

            if not node:
                return -1

            if node == target:

                collect_k_down(node, k)

                return 1

            left_dist = find_target_dist(node.left)

            if left_dist != -1:

                if left_dist == k:
                    ans.append(node.val)

                else:
                    collect_k_down(
                        node.right,
                        k - left_dist - 1
                    )

                return left_dist + 1

            right_dist = find_target_dist(node.right)

            if right_dist != -1:

                if right_dist == k:
                    ans.append(node.val)

                else:
                    collect_k_down(
                        node.left,
                        k - right_dist - 1
                    )

                return right_dist + 1

            return -1

        find_target_dist(root)

        return ans