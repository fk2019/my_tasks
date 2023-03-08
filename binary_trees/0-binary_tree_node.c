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
	parent = malloc(sizeof(binary_tree_t));
	parent->n = value;
	parent->left = NULL;
	parent->right = NULL;
	if (parent->left == NULL)
		parent->left = binary_tree_node(parent->left, value);
	else if (parent->right == NULL)
		parent->right = binary_tree_node(parent->right, value);
	return parent;
}
