"""
start: 7:17 pm
end: 7:50 pm

Time to map out problem on ipad too :fire

Graph Problem
numRouters is representative of the number of nodes
numLinks is the number of edges


Initially we assume that it is a connected graph
We need to figure out which nodes we remove
result in an unconnected graph

"""

from collections import defaultdict

def bfs(router_map, exclude_router) -> int:

    num_routers_discovered = 0
    queue = [router_map[exclude_router][0]]
    visited_routers = [queue[0]]

    while queue:

        router = queue.pop(0)

        # Enqueue this router's neighbors
        neighbors = router_map[router]
        for neighbor in neighbors:
            if neighbor not in visited_routers\
                and neighbor != exclude_router:
                queue.append(neighbor)
                visited_routers.append(neighbor)

        num_routers_discovered += 1

    return num_routers_discovered


def critical_routers(numRouters, numLinks, links):

    router_map = defaultdict(list)
    for src, dest in links:
        router_map[src].append(dest)
        router_map[dest].append(src)
    
    routers = list(range(1, numRouters + 1))

    routers_needing_upgrade = []
    for router in routers:
        # exclude this router from the bfs search
        num_routers_discovered = bfs(router_map, router)

        if num_routers_discovered != numRouters - 1:
            routers_needing_upgrade.append(router)
    return routers_needing_upgrade

if __name__ == "__main__":
    numRouters = 7
    numLinks = 7
    links = [[1, 2], [1, 3], [2, 4], [3, 4], [3, 6], [6, 7], [4, 5]]
    result = critical_routers(numRouters, numLinks, links)