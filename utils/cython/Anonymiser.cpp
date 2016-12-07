//
// Created by janos4276 on 05/12/16.
//

#include "Anonymiser.h"

#include <cstring>
#include <iomanip>
#include <sstream>

using adelost::Anonymiser;

Anonymiser::Anonymiser(const std::string& salt):
        m_ctx(::EVP_MD_CTX_create()),
        m_salt(salt)
{
    clear_digest();
}

Anonymiser::~Anonymiser()
{
    ::EVP_MD_CTX_destroy(m_ctx);
}

int Anonymiser::hash(const std::string& pii)
{
    clear_digest();

    if ( init() == 0)
    {
        return -1;
    }

    if (update(pii) == 0)
    {
        return -2;
    }

    if (update(m_salt) == 0)
    {
        return -3;
    }

    if (final_digest() == 0)
    {
        return -4;
    }

    return 0;
}

std::string Anonymiser::digest() const
{
    return to_hex_string(reinterpret_cast<const unsigned char* const>(&m_digest), m_bytes_to_read);
}

int Anonymiser::init() const
{
    return ::EVP_DigestInit_ex(m_ctx, ::EVP_sha256(), nullptr);
}

int Anonymiser::update(const std::string& data) const
{
    return ::EVP_DigestUpdate(m_ctx, data.c_str(), data.size());
}

int Anonymiser::final_digest()
{
    return ::EVP_DigestFinal_ex(m_ctx, m_digest, &m_bytes_to_read);
}

void Anonymiser::clear_digest()
{
    std::memset(&m_digest, 0, EVP_MAX_MD_SIZE);
    m_bytes_to_read = 0u;
}
