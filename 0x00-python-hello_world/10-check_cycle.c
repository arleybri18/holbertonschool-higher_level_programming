#include "lists.h"
#include <stdio.h>
/**
 *check_cycle - check if linked list is a cycle
 *
 *@list: head of the list
 *Return: 1 if linked list has a cycle, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *node_a = list;
	listint_t *node_b = list->next;

	while (node_a->next != NULL)
	{
		while (node_b->next != NULL)
		{
			if (node_a->n == node_b->n)
			{
				return (1);
			}
			node_b = node_b->next;
		}
		node_a = node_a->next;
	}
	return (0);


}
