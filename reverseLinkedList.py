def reverseLinkedList(cur):
    if not 'next' in cur:
	    return

    reverseLinkedList(cur['next'])
    cur['next']['next'] = cur
	
    del cur['next']
