#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
typedef struct listint_s
{
	int n;

	struct listint_s *next;
} listint_t;

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @**head: a pointer to the pointer head
 * @*slow: a pointer to slow
 * @*fast: a pointer to fast
 * @next: points to next
 * @prev: points to previous
 * @curr: points to current
 * Return: On success return 1
*/
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
	{
		return 1;
	}

	listint_t *slow = *head;
	listint_t *fast = *head;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	listint_t *prev = NULL;
	listint_t *curr = slow;
	listint_t *next;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	listint_t *l = *head;
	listint_t *r = prev;

	while (r != NULL)
	{
		if (l->n != r->n)
		{
			return 0;
		}
		l = l->next;
		r = r->next;
	}
	return 1;
}
