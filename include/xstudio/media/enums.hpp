// SPDX-License-Identifier: Apache-2.0
#pragma once

namespace xstudio {
namespace media {

    enum MediaType { MT_IMAGE = 0x1L, MT_AUDIO = 0x2L };
    enum MediaStatus {
        MS_ONLINE      = 0x0L,
        MS_MISSING     = 0x01L,
        MS_CORRUPT     = 0x02L,
        MS_UNSUPPORTED = 0x03L,
        MS_UNREADABLE  = 0x04L
    };

} // namespace media
} // namespace xstudio
