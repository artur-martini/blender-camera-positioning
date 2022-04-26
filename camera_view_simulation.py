import open3d as o3d



def main():
    print('camera view simulation')

    path = './cube.stl'
    mesh = o3d.io.read_triangle_mesh(path)

    pcd = mesh.sample_points_uniformly(number_of_points=10000)


    alpha = 0.03
    new_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(pcd, alpha)
    new_mesh.compute_vertex_normals()

    o3d.visualization.draw_geometries([new_mesh])    


if __name__ == "__main__":
    main()
