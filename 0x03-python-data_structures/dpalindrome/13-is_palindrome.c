#include "lists.h"
/**
 *add_dnodeint_end - add node at the beginning of a list
 *
 *@head: head of the list
 *@n: data for the node at the list
 *Return: address of the new element
 */

dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new_node = NULL;
	dlistint_t *aux = *head;

	new_node = malloc(sizeof(dlistint_t));
	if (new_node == NULL)
	{
		free(new_node);
		return (NULL);
	}

	if (*head == NULL)
	{
		*head = new_node;
		new_node->n = n;
		new_node->next = NULL;
		new_node->prev = NULL;
		return (*head);
	}

	while (aux->next != NULL)
		aux = aux->next;

	new_node->n = n;
	new_node->next = NULL;
	new_node->prev = aux;
	aux->next = new_node;

	return (*head);
}

/**
 *list_len - return a length
 *
 *@head: head of the list
 *Return: length of the ist
 */

int list_len(dlistint_t *head)
{
	int len;

	while (head != NULL)
	{
		head = head->next;
		len++;
	}
	return (len);
}

/**
 * is_palindrome - validate if list is a palindrome
 *
 * @head: head of the list
 * Return: return 0 if not is palindrome, 1 is if it
 */

int is_palindrome(listint_t **head)
{
	listint_t *aux;
	dlistint_t *h;
	dlistint_t *last, *begin;
	int i = 0, j = 0, flag = 0;

	h = NULL;
	aux = *head;
	while (aux)
	{
		add_dnodeint_end(&h, aux->n);
		aux = aux->next;
	}
	begin = h;
	last = h;
	j = list_len(h);
	while (last->next != NULL)
		last = last->next;
	while (last->prev != NULL && begin->next != NULL)
	{
		if (i == j)
			break;
		if (begin->n != last->n)
			flag = 1;
		begin = begin->next;
		last = last->prev;
		i++;
		j--;
	}
	if (flag != 0)
	{
		free_listint(h);
		return (0);
	}
	free_listint(h);
	return (1);
}
