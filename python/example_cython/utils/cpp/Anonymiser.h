//
// Created by janos4276 on 05/12/16.
//

#ifndef UTILS_ANONYMISER_H
#define UTILS_ANONYMISER_H

#include <openssl/evp.h>

#include <string>

namespace adelost
{
    constexpr unsigned char hex_map[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};

    inline std::string to_hex_string(const unsigned char* const data,  const std::size_t length)
    {
        std::string hex(length * 2, ' ');
        for (unsigned int i = 0u; i < length; ++i)
        {
            hex[2*i] = hex_map[(data[i] & 0xf0) >> 4];
            hex[2*i + 1] = hex_map[(data[i] & 0x0f)];
        }

        return hex;
    }

    class Anonymiser final
    {
    public:
        explicit Anonymiser(const std::string& salt = std::string());

        ~Anonymiser();

        int hash(const std::string& pii);

        std::string digest() const;

    private:
        int init() const;

        int update(const std::string& data) const;

        int final_digest();

        void clear_digest();

    private:
        unsigned char m_digest[EVP_MAX_MD_SIZE];
        unsigned int m_bytes_to_read{0u};
        using HasherContext = ::EVP_MD_CTX;
        HasherContext* m_ctx{nullptr};
        std::string m_salt{std::string()};
    };
}

#endif //UTILS_ANONYMISER_H
