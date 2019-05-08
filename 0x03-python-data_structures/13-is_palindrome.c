#include "lists.h"

/**
 *list_len - return a length
 *
 *@head: head of the list
 *Return: length of the ist
 */

int list_len(listint_t *head)
{
	int len = 0;

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
	listint_t *h;
	int array[10000];
	int i = 0, j = 0;

	if (head == NULL)
		return (1);
	h = *head;
	aux = *head;
	j = list_len(h) - 1;
	while (aux)
	{
		array[i] = aux->n;
		aux = aux->next;
		i++;
	}
	for (i = 0; i < j; i++, j--)
	{
		if (array[i] != array[j])
			return (0);
	}
	return (1);
}
