find_package(fmt REQUIRED)
find_package(Imath REQUIRED)

SET(LINK_DEPS
	caf::io
	caf::core
	fmt::fmt
        nlohmann_json::nlohmann_json
        spdlog::spdlog
        Imath::Imath
)

create_component(caf_utility 0.1.0 "${LINK_DEPS}")

