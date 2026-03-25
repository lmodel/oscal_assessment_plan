package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Describes either recommended or an actual plan for addressing the risk.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Response  {

  private String uuid;
  private String title;
  private String description;
  private String lifecycle;
  private List<Origin> origins;
  private List<RequiredAsset> required-assets;
  private List<Task> tasks;
  private String remarks;
  private List<Property> props;
  private List<Link> links;

}