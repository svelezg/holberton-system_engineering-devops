#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - creates an infinite loop
 *
 * Return: always 0 (success)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point
 *
 * Return: always 0 (success)
 */
int main(void)
{
	pid_t zombie_pid;
	unsigned int i;

	for (i = 0; i < 5; i++)
	{
		zombie_pid = fork();
		if (zombie_pid == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %ld\n", (long) zombie_pid);
	}
	infinite_while();
	return (0);
}
