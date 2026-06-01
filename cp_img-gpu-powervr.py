import os
import shutil
import glob


def copy_firmware(source_dir, destination_dir):
	# 确保目标目录存在
	if not os.path.exists(destination_dir):
		print("目标路径: {destination_dir} 不存在，请确认！")
		return 0

	cure_path = "binary_fpga_linux_wayland_release/target_neutral"
	cur_files = ["rgx.fw.36.56.104.183", "rgx.sh.36.56.104.183"]

    # 复制文件
	for file in cur_files:
		shutil.copy(os.path.join(source_dir, cure_path, file), os.path.join(destination_dir, file))
        
	print(f"Copied {cur_files} to {destination_dir}")


def copy_usr(source_dir, destination_dir):
	# 确保目标目录存在
	if not os.path.exists(destination_dir):
		print("目标路径: {destination_dir} 不存在，请确认！")
		return 0

	cure_path = "binary_fpga_linux_wayland_release/target_riscv64"
	cur_files = ['libGLESv1_CM_PVR_MESA.so',
				'libGLESv2_PVR_MESA.so',
				'libPVRScopeServices.so',
				'libglslcompiler.so',
				'libpvr_dri_support.so',
				'libsrv_um.so',
				'libusc.so',
				'libPVROCL.so',
				'libPVROCL.so.1',
				'libufwriter.so',
				'libVK_IMG.so',
				'libVK_IMG.so.1',
				'libsutu_display.so']

	cur_files += [_.split('.')[0]+'.dbg' for _ in cur_files]

	# 复制文件
	for file in cur_files:
		shutil.copy(os.path.join(source_dir, cure_path, file), os.path.join(destination_dir, file))

	cure_path = "binary_fpga_linux_wayland_release/target_riscv64/usr/local/lib"
	cur_files = ["libvulkan.so", "libvulkan.so.1", "libvulkan.so.1.3.280"]
	for file in cur_files:
		shutil.copy(os.path.join(source_dir, cure_path, file), os.path.join(destination_dir, file))

	print(f"Copied {cur_files} to {destination_dir}")


def copy_txtFiles(source_dir, destination_dir):
	# 确保目标目录存在
	if not os.path.exists(destination_dir):
		print("目标路径: {destination_dir} 不存在，请确认！")
		return 0

	cure_path = "unittests"
	cur_files = glob.glob(os.path.join(source_dir, cure_path, "**/**/*.txt"))

    # 复制文件
	for file in cur_files:
		shutil.copy(file, os.path.join(destination_dir, os.path.basename(file)))
        
	print(f"Copied {cur_files} to {destination_dir}")


def copy_etc(source_dir, destination_dir):
	# 确保目标目录存在
	if not os.path.exists(destination_dir):
		print("目标路径: {destination_dir} 不存在，请确认！")
		return 0

	cure_path = "binary_fpga_linux_wayland_release/target_neutral"
	cur_files = ["powervr_icd.json"]

    # 复制文件
	for file in cur_files:
		shutil.copy(os.path.join(source_dir, cure_path, file), os.path.join(destination_dir, file))
        
	print(f"Copied {cur_files} to {destination_dir}")


def copy_bin(source_dir, destination_dir):
	# 确保目标目录存在
	if not os.path.exists(destination_dir):
		print("目标路径: {destination_dir} 不存在，请确认！")
		return 0

	cur_files = ['eglconfigs',
				'ggles2test1',
				'gles1image_external',
				'gles3_render_to_image',
				'ocl_unit_test',
				'pvrhwperf',
				'pvrsrvctl',
				'rgx_kicksync_test',
				'rogue2d_unittest',
				'wgles1test1',
				'wvkcompute',
				'egldmabuf',
				'ggles3driimage',
				'gles1test1',
				'gles3test1',
				'pvrdebug',
				'pvrlogdump',
				'pvrtld',
				'rgx_triangle_test',
				'tqplayer',
				'wgles2test1',
				'wvksalut',
				'geglinfo',
				'ggles3eglimage',
				'gles2test1',
				'hwperfbin2jsont',
				'pvrhtb2txt',
				'pvrlogsplit',
				'rgx_blit_test',
				'rgx_twiddling_test',
				'weglinfo',
				'wgles3test1',
				'ggles1test1',
				'ggles3test1',
				'gles3image_external',
				'ocl_extended_test',
				'pvrhtbd',
				'pvr_memory_test',
				'rgx_compute_test',
				'rogue2d_fbctest',
				'wgles1image_external',
				'wvkbonjour']

	cur_files += [_.split('.')[0]+'.dbg' for _ in cur_files]

	# 用于记录不存在的文件
	missing_files = []
	cure_path = "binary_fpga_linux_wayland_release/target_riscv64/"
	# 搜索并复制文件
	for root, dirs, files in os.walk(os.path.join(source_dir, cure_path)):
		for file in files:
			if file in cur_files:
				source_path = os.path.join(root, file)
				target_path = os.path.join(destination_dir, file)
				shutil.copy(source_path, target_path)
				# print(f"Copied {source_path} to {target_path}")
				cur_files.remove(file)  # 从列表中移除已找到的文件

	cure_path = "unittests"
	# 在单元测试文件夹再搜索一次
	for root, dirs, files in os.walk(os.path.join(source_dir, cure_path)):
		for file in files:
			if file in cur_files:
				source_path = os.path.join(root, file)
				target_path = os.path.join(destination_dir, file)
				shutil.copy(source_path, target_path)
				# print(f"Copied {source_path} to {target_path}")
				cur_files.remove(file)  # 从列表中移除已找到的文件

	# 检查并打印不存在的文件
	if cur_files:
		print("The following files were not found:", cur_files)

	else:
		print("All files were found and copied successfully.")

	# print(f"Copied {cur_files} to {destination_dir}")



if __name__ == "__main__":
	# 指定源目录和目标目录
	source_dir = ''

	# 调用函数复制文件
	copy_firmware(source_dir, "./target/lib/firmware/")

	copy_usr(source_dir, "./target/usr/lib/")

	copy_txtFiles(source_dir, "./target/usr/local/share/pvr/shaders/")

	copy_etc(source_dir, "./target/etc/vulkan/icd.d/")

	copy_bin(source_dir, "./target/usr/local/bin/")

