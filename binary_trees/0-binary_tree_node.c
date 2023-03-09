#include "binary_trees.h"
#include <stdio.h>

/**
 * binary_tree_node - Create a binary tree
 * @parent: parent node pointer
 * @value: node value
 *
 * Return: pointer to new node otherwise NULL
 */
binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
	binary_tree_t *node;

	node = malloc(sizeof(binary_tree_t));
	if (node == NULL)
	{
		perror("malloc");
		return (NULL);
	}
	node->n = value;
	node->left = NULL;
	node->right = NULL;
	node->parent = parent;

	return node;
}
