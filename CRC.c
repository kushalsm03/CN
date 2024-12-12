#include <stdio.h>
#include <string.h>

#define N strlen(gen_poly)

char data[28], check_value[28], gen_poly[10];
int data_length;

void XOR() {
    for (int j = 1; j < N; j++)
        check_value[j] = (check_value[j] == gen_poly[j]) ? '0' : '1';
}

void crc() {
    for (int i = 0; i < N; i++)
        check_value[i] = data[i];

    for (int i = N; i <= data_length + N - 1; i++) {
        if (check_value[0] == '1')
            XOR();

        for (int j = 0; j < N - 1; j++)
            check_value[j] = check_value[j + 1];

        check_value[N - 1] = data[i];
    }
}

void receiver() {
    printf("Enter the received data: ");
    scanf("%s", data);
    printf("\n-----------------------------\n");
    printf("Data received: %s\n", data);

    crc();

    if (strchr(check_value, '1'))
        printf("\nError detected\n\n");
    else
        printf("\nNo error detected\n\n");
}

int main() {
    printf("Enter data to be transmitted: ");
    scanf("%s", data);

    printf("\nEnter the Generating polynomial: ");
    scanf("%s", gen_poly);

    data_length = strlen(data);

    strcat(data, "000");
    printf("\n----------------------------------------");
    printf("\nData padded with n-1 zeros: %s", data);
    printf("\n----------------------------------------");

    crc();

    printf("\nCRC or Check value is: %.*s", (int)(N-1), check_value);

    strncat(data, check_value, N-1);
    printf("\n----------------------------------------");
    printf("\nFinal data to be sent: %s", data);
    printf("\n----------------------------------------\n");

    receiver();

    return 0;
}
