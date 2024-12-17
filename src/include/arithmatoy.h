#pragma once

extern int VERBOSE;
char *arithmatoy_add(unsigned int base, const char *lhs, const char *rhs);

char *arithmatoy_sub(unsigned int base, const char *lhs, const char *rhs);

char *arithmatoy_mul(unsigned int base, const char *lhs, const char *rhs);

void arithmatoy_free(char *number);
