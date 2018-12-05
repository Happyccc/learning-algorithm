int LCS_recursion(char* A, int n, char* B, int m)
{
	if (n <= 0 || m <= 0)	//��A��BΪ������ʱ���ݹ��
		return 0;
	else if (A[n - 1] == B[m - 1])	// ��A��Bĩ�ַ���ͬʱ��������֮
		return LCS_recursion(A, n - 1, B, m - 1) + 1;
	else							// ��A��Bĩ�ַ�����ͬʱ���ֶ���֮
		return max(LCS_recursion(A, n - 1, B, m), LCS_recursion(A, n, B, m - 1));
}

int LCS_iteration(char* A, int n, char* B, int m)
{
	int** record = new int*[n + 1];
	for (int i = 0; i < n + 1; ++i)		// ��ʼ����ά��
		record[i] = new int[m + 1]();

	for (int i = 1; i < n + 1; ++i)
	{
		for (int j = 1; j < m + 1; ++j)
		{
			if (A[i - 1] == B[j - 1])
				record[i][j] = record[i - 1][j - 1] + 1;
			else
				record[i][j] = max(record[i - 1][j], record[i][j - 1]);
		}
	}
	return record[n][m];
}